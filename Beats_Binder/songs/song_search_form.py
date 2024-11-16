from django import forms

# When we will have a database, instead of having ("Keanu Reeves", "Keanu Reeves"),
# we will have (1, "Keanu Reeves") for example with 1 the id of "Keanu Reeves" in the database

class SongSearchForm(forms.Form):
   Search = forms.CharField(max_length=200, required=True)
   
# def clean(self):
#    cleaned_data = super().clean()
#    actors = cleaned_data.get('actors', [])
#    if "Keanu Reeves" in actors and "Scarlett Johanson" in actors:
#       msg = "Scarlett Johanson never acted with Keanu Reeves"
#       raise forms.ValidationError(msg)
#    return cleaned_data

