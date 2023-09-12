from vkbottle import BaseStateGroup


class StartState(BaseStateGroup):
    CITY = "city"


class TodayTomorrowState(BaseStateGroup):
    WHEN = "когда"
