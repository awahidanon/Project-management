from rest_framework import serializers

from .models import Catagory, ProjectInfo


class CatagorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Catagory
        fields = ["name"]


class ProjectInfoSerializer(serializers.HyperlinkedModelSerializer):
    catagory = CatagorySerializer()

    class Meta:
        model = ProjectInfo
        fields = [
            "project_name",
            "catagory",
            "zone",
            "woreda",
            "price",
            "rebate",
            "price_after_rebate",
            "vat",
            "after_vat",
            "consultant",
            "start_date",
            "end_date",
            "update",
        ]

    rebate = serializers.SerializerMethodField(method_name="Rebate")
    price_after_rebate = serializers.SerializerMethodField(method_name="AfterRebate")
    vat = serializers.SerializerMethodField(method_name="VatCalculation")
    after_vat = serializers.SerializerMethodField(method_name="AfterVatCalculation")

    def AfterVatCalculation(self, ProjectInfo):
        return ProjectInfo.price - ProjectInfo.price * 15 / 100

    def VatCalculation(self, ProjectInfo):
        return ProjectInfo.price * 15 / 100

    def Rebate(self, ProjectInfo):
        return ProjectInfo.price * ProjectInfo.rebate / 100

    def AfterRebate(self, ProjectInfo):
        return ProjectInfo.price - ProjectInfo.price * ProjectInfo.rebate
