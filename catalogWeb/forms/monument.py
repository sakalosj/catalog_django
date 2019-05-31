from django import forms

from catalogWeb.models import Monument, SelectDateWidget2, Monument2Material


class MonumentForm(forms.ModelForm):
    class Meta:
        model = Monument
        exclude = ['materialList', 'album']
        # MaterialList = forms.ModelMultipleChoiceField(queryset=MaterialList.objects.filter(materials__material2materiallist__materialList_id__exact= 1))

    date = forms.DateField(widget=SelectDateWidget2)

    def save(self, *args, **kwargs): #, album, commit=True):
        # self.instance.album = album
        self.instance.save()

        Monument2Material.objects.filter(monument=self.instance.id).delete()
        for material in self.cleaned_data.get('materials'):
            Monument2Material.objects.create(material=material, monument=self.instance, description='TEST')

        files = self.cleaned_data.get('pictures')


        # for file in files:
        #     image = Image(files)
        #     album.save()
        #     Image.objects.create(name=file, description=file, image=file, album=self.instance.album)

        return self.instance

