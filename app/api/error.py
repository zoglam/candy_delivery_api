from fastapi.responses import JSONResponse


class APIError:

    @staticmethod
    def create_courier_error(error_list):
        return JSONResponse(
            {'validation_error': {'couriers': error_list}},
            status_code=400
        )
