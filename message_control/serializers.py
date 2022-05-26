from .models import GenericFileUpload, Message, MessageAttachment
from rest_framework import serializers


#serializer handling generic file uploads (profile pics, docs etc..)
class GenericFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericFileUpload
        fields = "__all__"


# handling messages with attachments

class MessageAttachmentSerializer(serializers.ModelSerializer):
    attachment = GenericFileUploadSerializer()  # calls generic file upload seraializer in case of file upload
    class Meta:
        model = MessageAttachment
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField("get_user_data")
    sender_id = serializers.IntegerField(write_only=True)
    receiver = serializers.SerializerMethodField("get_user_data")
    receiver_id = serializers.IntegerField(write_only=True)
    message_attachmets = MessageAttachmentSerializer(read_only=True,many=True)

    class Meta:
        model = Message
        fields = "__all__"

    # gets the data of user from user_control (for both sender and receiver)

    def get_user_data(self,obj):
        from user_control.serializers import UserProfileSerializer
        return UserProfileSerializer(obj.sender.user_profile)

