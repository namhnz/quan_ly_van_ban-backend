from db_client import db
from app import app
from flask import jsonify, request
from ultis.convert_to_json import convertToJson
from bson.objectid import ObjectId


@app.route('/van_ban_den/add_one', methods=['POST'])
def vanBanDenAddOne():
    input_json = request.get_json(force=True)

    # db.vanBanDen.insert_one(
    #     {"ngayThang": "28/11/2022", "soVanBan": "483ĐK:HT", "noiDung": "Rà soát trùng số CMND"})

    print('Dữ liệu được gửi lên: ', input_json)
    db.vanBanDen.insert_one(input_json)

    return jsonify(message="success")


@app.route('/van_ban_den/all')
def vanBanDenFindAll():
    allVanBanDens = db.vanBanDen.find()
    return convertToJson([vanBanDen for vanBanDen in allVanBanDens])

@app.route('/van_ban_den/<id>', methods=['DELETE'])
def vanBanDenDeleteOne(id):
    print("Id được yêu cầu xoá: ", id)
    deleteResult = db.vanBanDen.delete_one({"_id": ObjectId(id)})
    print("Number of documents deleted: ", deleteResult.deleted_count)

    return jsonify(message="success");

@app.route('/van_ban_den/<id>', methods=['PUT'])
def vanBanDenUpdateOne(id):
    input_json = request.get_json(force=True)
    print('Dữ liệu được cập nhật: ', input_json)

    db.vanBanDen.update_one({"_id": ObjectId(id)}, {
        "$set": input_json
    })
    
    return jsonify(message="success")