from flask import  jsonify
from .models import Error
from .serializers import ErrorSerializer
from .urls import bp


@bp.route("/errors", methods=["GET"])
def get_errors():
    errors = [Error("Error 1", "Description 1"), Error("Error 2", "Description 2")]
    serializer = ErrorSerializer(errors)
    return jsonify([serializer.serialize() for serializer in serializer])


@bp.route("/errors/<int:error_id>", methods=["GET"])
def get_error(error_id):
    error = Error("Error " + str(error_id), "Description " + str(error_id))
    serializer = ErrorSerializer(error)
    return jsonify(serializer.serialize())
