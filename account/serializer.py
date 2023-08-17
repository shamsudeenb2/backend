from .models import Profile
from rest_framework import serializers

class ImageUrlField(serializers.ReadOnlyField):
    def to_representation(self, value):
        if value:
            request = self.context.get('request')
            image_url = value.url
            return request.build_absolute_uri(image_url)
        return None

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        json_data = validated_data.pop('json_data') if 'json_data' in validated_data else None
        profile_img = validated_data.pop('profile_img') if 'profile_img' in validated_data else None

        # Create the Profile instance using the validated_data
        profile = Profile.objects.create(**validated_data)

        if json_data:
            # Set fields using json_data
            profile.sickness_name = json_data['sickness_name']
            profile.gender = json_data['gender']

        if profile_img:
            # Handle profile_img upload here (save to profile.profile_img field)
            profile.profile_img.save(profile_img.name, profile_img, save=True)

        return profile
