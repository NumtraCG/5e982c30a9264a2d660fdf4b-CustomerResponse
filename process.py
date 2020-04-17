import json
import Connectors
import Transformations
import AutoML
try:
    CustomerResponse_DBFS = Connectors.DBFSConnector.fetch(
        [], {}, "5e982c30a9264a2d660fdf4c", spark, "{'url': '/Demo/CustomerResponseTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapib8073bbfa952efa9d363b234ce06e2c6', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    CustomerResponse_AutoFE = Transformations.TransformationMain.run(["5e982c30a9264a2d660fdf4c"], {"5e982c30a9264a2d660fdf4c": CustomerResponse_DBFS}, "5e982c30a9264a2d660fdf4d", spark, json.dumps({"FE": [{"transformationsData": {}, "feature": "Distance_from_nearest_store", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "4078", "mean": "4.98", "stddev": "2.88", "min": "0.014165387", "max": "10.00734672", "missing": "0"}, "transformation": ""}, {"transformationsData": {"feature_label": "Mosaic_group"}, "feature": "Mosaic_group", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "4078", "mean": "", "stddev": "", "min": "A", "max": "S", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Amount_purchased_6m", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "4078", "mean": "408.95", "stddev": "285.33", "min": "0.0", "max": "1233.13", "missing": "0"}, "transformation": ""}, {
                                                                     "transformationsData": {"feature_label": "Mosaic_likelihood"}, "feature": "Mosaic_likelihood", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "4078", "mean": "", "stddev": "", "min": "Average", "max": "Unlikely", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Purchased_sale_soda", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "4078", "mean": "0.49", "stddev": "0.5", "min": "0", "max": "1", "missing": "0"}}, {"feature": "Mosaic_group_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "4078", "mean": "7.05", "stddev": "5.4", "min": "0.0", "max": "18.0", "missing": "0"}}, {"feature": "Mosaic_likelihood_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "4078", "mean": "0.82", "stddev": "0.76", "min": "0", "max": "2", "missing": "0"}}]}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionClassification(CustomerResponse_AutoFE, [
                                  "Distance_from_nearest_store", "Mosaic_group", "Amount_purchased_6m", "Mosaic_likelihood"], "Purchased_sale_soda")

except Exception as ex:
    print(ex)
