from django import forms
import os


class GetSummonerForm(forms.Form):
    sum_name = forms.CharField(label='Summoner Name')
class GetMultiSummonerForm(forms.Form):
    sum_name = forms.CharField(label="Summoners Name", widget=forms.Textarea(attrs={'placeholder': f"IMP Dyemon joined the room.{os.linesep}\
IMP Jean Pol joined the room.{os.linesep}\
IMP Cartman joined the room.{os.linesep}\
IMP Orange joined the room."}))
