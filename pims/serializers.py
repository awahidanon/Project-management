from rest_framework import serializers
from .models import Catagory, ProjectInfo


class CatagorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Catagory
        fields = [ 'name']

class ProjectInfoSerializer(serializers.HyperlinkedModelSerializer):
    catagory = CatagorySerializer()

    class Meta:
        model = ProjectInfo
        fields = ['project_Name','catagory', 'zone', 'woreda','price','Rebatee','Price_After_Rebate','vat','afterVat','consultant','startDate', 'endDate', 'update']

    Rebatee = serializers.SerializerMethodField(method_name='Rebate')
    Price_After_Rebate = serializers.SerializerMethodField(method_name='After_Rebate')
    vat = serializers.SerializerMethodField(method_name='vatCalculation')
    afterVat = serializers.SerializerMethodField(method_name='AftervatCalculation')
    

    def AftervatCalculation(self, ProjectInfo):
        
        return ProjectInfo.price - ProjectInfo.price * 15/100
           
    def vatCalculation(self, ProjectInfo):
        return ProjectInfo.price * 15/100
    
    def Rebate(self, ProjectInfo):
        return ProjectInfo.price * ProjectInfo.Rebate/100
   
    
    def After_Rebate (self, ProjectInfo):
         return ProjectInfo.price - ProjectInfo.price * ProjectInfo.Rebate
    
   
    

  