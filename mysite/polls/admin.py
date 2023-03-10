from django.contrib import admin

# Register your models here.
from .models import Question,Role,User,Candidate,Election,Vote,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Candidate)
admin.site.register(Election)
admin.site.register(Vote)
