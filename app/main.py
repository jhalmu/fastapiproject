from fastapi import BackgroundTasks, FastAPI

from .config import MailBody
from .mailer import send_mail

app = FastAPI()


@app.get("/")
def index():
    return {"status": "fastapi server is running."}


@app.post("/send-email")
def schedule_mail(req: MailBody, tasks: BackgroundTasks):
    data = req.dict()
    tasks.add_task(send_mail, data)
    return {"status": 200, "message": "email has been scheduled."}
