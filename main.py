#!flask/bin/python
from flask import Flask, jsonify, request
import json
import os
import traceback
from scoring.scorer import RandomScorer
from product.productrepo import FileProductRepository
from product.userfilter import UserFilter

PROD_ID_TAG = "ProdId"
PRICE_RANGE_TAG = "PriceRange"
PRICE_RANGE_FROM_TAG = "from"
PRICE_RANGE_TO_TAG = "to"
IS_BASE_TAG = "IsBase"
SCORE_TAG = "Score"
PRODUCT_TAG = "Product"

scorer = RandomScorer()
repo = FileProductRepository(os.environ['DATA_PATH'])
app = Flask(__name__)


@app.route('/msb/getscore', methods=['POST'])
def get_score():
    try:
        k = request.form.keys()
        for t in request.form.keys():
            print(t)
        print(request.form)
        indata = json.loads(request.data.decode("utf-8"))
        if PROD_ID_TAG in indata:
            productId = indata[PROD_ID_TAG]
            pricefrom = None
            priceto = None
            if PRICE_RANGE_TAG in indata:
                pricerange = indata[PRICE_RANGE_TAG]
                if PRICE_RANGE_FROM_TAG in pricerange:
                    pricefrom = float(pricerange[PRICE_RANGE_FROM_TAG])
                if PRICE_RANGE_TO_TAG in pricerange:
                    priceto = float(pricerange[PRICE_RANGE_TO_TAG])
            baseproduct = repo.getProductByItemId(productId)
            if baseproduct is None:
                return jsonify({'error': "Product not found"})
            userfilter = UserFilter(
                baseproduct.getCategoryTree(), 10, pricefrom, priceto)
            otherproducts = repo.getProductsByUserFilter(userfilter)
            out = {}
            results = []
            scores = [scorer.getScore(p) for p in otherproducts]
            isbase = [p.getItemId() == productId for p in otherproducts]
            for i in range(len(otherproducts)):
                results.append(
                    {
                        IS_BASE_TAG: isbase[i],
                        SCORE_TAG: scores[i],
                        PRODUCT_TAG: otherproducts[i].raw
                    })
            out["results"] = results
            return jsonify(out)
        else:
            return jsonify({'error': "Product id not specified"})
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()})


@app.route('/msb/getproduct', methods=['GET'])
def get_product():
    productid = request.args.get('productid', default=None, type=str)
    if productid is None:
        return jsonify({"error": "Product id must be specified"})
    product = repo.getProductByItemId(productid)
    if product is None:
        return jsonify({"error": "Product not found"})
    return jsonify({"product": product.raw})


if __name__ == '__main__':
    print(os.environ['FLASK_APP'])
    app.run(debug=True)
