#!flask/bin/python
from flask import Flask, jsonify, request
from flask.ext.cors import CORS
import json
import os
import traceback
from scoring.scorer import RandomScorer, CategoryScorer
from product.productrepo import FileProductRepository
from product.userfilter import UserFilter

PROD_ID_TAG = "ProdId"
PRICE_RANGE_TAG = "PriceRange"
PRICE_RANGE_FROM_TAG = "from"
PRICE_RANGE_TO_TAG = "to"
IS_BASE_TAG = "IsBase"
SCORE_TAG = "Score"
PRODUCT_TAG = "Product"
DIFFS_TAG = "Diff"
USER_PREFERENCES_TAG = "UserPrefs"
PREF_CATEGORY_TAG = "PrefCategory"
PREF_STRENGTH_TAG = "PrefStrength"

scorer = CategoryScorer()
repo = FileProductRepository(os.environ['DATA_PATH'])
app = Flask(__name__)

CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/msb/getscore', methods=['POST'])
def get_score():
    try:
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
            preferences = {}
            if USER_PREFERENCES_TAG in indata:
                userprefs = indata[USER_PREFERENCES_TAG]
                for userpref in userprefs:
                    preferences[userpref[PREF_CATEGORY_TAG]] = float(userpref[PREF_STRENGTH_TAG])
            baseproduct = repo.getProductByItemId(productId)
            if baseproduct is None:
                return jsonify({'error': "Product not found"})
            userfilter = UserFilter(
                baseproduct.getCategoryTree(), 2)
            otherproducts = repo.getProductsByUserFilter(userfilter)
            out = {}
            results = []
            scores, diffs = scorer.getScore(baseproduct, otherproducts, preferences)
            for i in range(len(otherproducts)):
                currentproduct = otherproducts[i]

                results.append(
                    {
                        IS_BASE_TAG: otherproducts[i].getItemId() == productId,
                        SCORE_TAG: scores[i],
                        PRODUCT_TAG: currentproduct.raw,
                        DIFFS_TAG: diffs[i]
                    })
            out["results"] = results
            out['params'] = scorer.mapper.get_ordered_params(baseproduct.getCategory())
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
    # print(os.environ['FLASK_APP'])
    app.run(debug=True)
