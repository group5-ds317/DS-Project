from django.db import models
from django.utils import timezone
from .course import Course

# Function to create the model dynamically
def create_phobert_model():
    # Generate 768 embedding dimension fields
    fields = {
        f'embedding_dim_{i}': models.FloatField(null=False, blank=False)
        for i in range(768)
    }
    # Add other fields to the model
    fields['course_id'] = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False)
    fields['created_at'] = models.DateTimeField(default=timezone.now)
    fields['updated_at'] = models.DateTimeField(default=timezone.now)
    fields['__str__'] = lambda self: str(self.course_id)
    fields['__module__'] = __name__  # Required for Django to recognize the model

    # Create and return the model class
    return type('PhoBERTParaphasedTomtat', (models.Model,), fields)

# Create the model
PhoBERTParaphasedTomtat = create_phobert_model()