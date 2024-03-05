from rest_framework import serializers
from app1.models import movies_model

class MovieSerializer(serializers.ModelSerializer):
    len_movie_name=serializers.SerializerMethodField()
    class Meta:
        model=movies_model
        fields="__all__"
    
    def validate_movie_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("Nameis too short!")
        else:
            return value
    
    # object validator
    def validate(self,data):
        if data['movie_name']==data['movie_description']:
            raise serializers.ValidationError("name and description should be different")
        else:
            return data
    
    def get_len_movie_name(self,object):
        return len(object.movie_name)


# validator
# def name_length(value):
#     if len(value)<2:
#             raise serializers.ValidationError("Nameis too short!")



# class MovieSerializer(serializers.Serializer):
#     movie_name=serializers.CharField(validators=[name_length])
#     movie_description=serializers.CharField()
#     movie_active=serializers.BooleanField()

#     def create(self,validated_data):
#         return movies_model.objects.create(**validated_data)
    
#     def update(self,instance,validated_data): # instance = old data , validated data= new data
#         instance.movie_name=validated_data.get('movie_name',instance.movie_name)
#         instance.movie_description=validated_data.get('movie_description',instance.movie_description)
#         instance.movie_active=validated_data.get('movie_active',instance.movie_active)
#         instance.save()
#         return instance
    
#     #field validator
#     def validate_movie_name(self,value):
#         if len(value)<2:
#             raise serializers.ValidationError("Nameis too short!")
#         else:
#             return value
    
#     # object validator
#     def validate(self,data):
#         if data['movie_name']==data['movie_description']:
#             raise serializers.ValidationError("name and description should be different")
#         else:
#             return data