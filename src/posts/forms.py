from django import forms
from posts.models import Posts


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        # fields = "__all__"
        exclude = ("created_by",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["name"].widget.attrs["class"] = "form-control"   this is used to customize single field
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    def clean_name(self):
        title = self.cleaned_data.get("title")
        if title.isdigit():
            raise forms.ValidationError("Title cannot be a number")
        return title
