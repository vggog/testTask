from vkbottle import BaseStateGroup


class StartState(BaseStateGroup):
    ISCORRECT = "isCorrect"
    SITY = "sity"
    UPLOADSITY = "uploadSity"


class TodayTomorrowState(BaseStateGroup):
    WHEN = "когда"
