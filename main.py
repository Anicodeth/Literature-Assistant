from litassist.controller.ai_controller import *
from litassist.configurations.api_configuration import *
import uvicorn

app.include_router(router, prefix = "/api/v1")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


