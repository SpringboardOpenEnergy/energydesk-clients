#from rest_framework.serializers import Serializer
#from rest_framework_money_field import MoneyField
#from rest_framework.renderers import JSONRenderer
#from moneyed import Money, USD, NOK, EUR


def gen_json_money(mon):

    json =  {
            "amount": float(mon.amount),
            "currency": str(mon.currency)
    }
    return json