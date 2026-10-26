from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from careers.models import Career
from careers.serializers import CareerSerializer
from .serializers import AssessmentSerializer, ChatSerializer

class AssessmentRecommendView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = AssessmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        selected = set(serializer.validated_data["interests"])
        results = []
        for career in Career.objects.all():
            tags = set(career.interests or [])
            overlap = len(selected & tags)
            score = round(100 * overlap / max(len(selected), 1))
            if overlap:
                results.append({"career": CareerSerializer(career).data, "match_score": score,
                                "matched_interests": sorted(selected & tags),
                                "explanation": "This option shares interests you selected. Use it to explore, not as a prediction of success."})
        results.sort(key=lambda x: x["match_score"], reverse=True)
        return Response({"results": results[:8], "notice": "Interest matches are exploratory. Eligibility has not been verified by this score."})

class ChatView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.validated_data["question"]
        # Safe baseline: this endpoint is deliberately not presented as RAG.
        # Replace with retrieval from approved, current education sources before production.
        return Response({
            "answer": "I can help you explore options. CareerPath AI's starter chatbot is not yet connected to a verified education knowledge base, so I cannot confirm current eligibility or admission rules. Tell me your class, state/board, favourite subjects and the career areas you are curious about; then use the Career Explorer to compare options. Please verify requirements with the relevant official board, institution or admission authority.",
            "question_received": question,
            "citations": [],
            "grounding_status": "not_connected"
        }, status=status.HTTP_200_OK)
