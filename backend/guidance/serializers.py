from rest_framework import serializers

class AssessmentSerializer(serializers.Serializer):
    interests = serializers.ListField(child=serializers.ChoiceField(choices=[
        "technology", "problem_solving", "mathematics", "biology", "helping_people",
        "business", "creativity", "visual_design", "research", "building", "communication", "detail"
    ]), allow_empty=False, max_length=12)
    current_class = serializers.IntegerField(min_value=8, max_value=12, required=False)
    state = serializers.CharField(required=False, allow_blank=True)
    board = serializers.CharField(required=False, allow_blank=True)

class ChatSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=1500)
