from django import forms

from . models import students, DistrictChoices,CourseChoices,BatchChoices,TrainerChoices

from batches.models import Batches

from courses.models import Courses

from trainers.models import Trainers

class StudentsRegisterForm(forms.ModelForm):

    class Meta:

        model = students 

        # fields = ['first_name','last_name','photo','email','contact_num','house_name',
        #       'post_office','district','pincode','course','batch','batch_date','trainer_name']
        
        # if all fields in the models used

        # fields = '_all_'

        exclude = ['admission_num','join_date','uuid','active_status','profile']

        widgets = {'first_name' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                         'placeholder' : 'Enter first name', 
                                                         'required' :'required'}),
                    'last_name' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter last name', 
                                                                    'required' :'required'}),
                    'photo' : forms.FileInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                }),
                    'email' : forms.EmailInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter email', 
                                                                    'required' :'required'}),
                    'contact_num' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter contact number', 
                                                                    'required' :'required'}),
                    'house_name' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter house name', 
                                                                    'required' :'required'}),
                    'post_office' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter post office', 
                                                                    'required' :'required'}),
                    'pincode' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter pincode', 
                                                                    'required' :'required'}),
                    # 'batch_date' : forms.DateInput(attrs={'type': 'date','class' : 
                    #                                       'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                    #                                                 'placeholder' : 'Enter batch date', 
                    #                                                 'required' :'required'}),

                                                                    }
    district = forms.ChoiceField(choices=DistrictChoices.choices,widget=forms.Select(attrs={
                                                                                    'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                    'required' : 'required'}))
    # course = forms.ChoiceField(choices=CourseChoices.choices,widget=forms.Select(attrs={
    #                                                                                 'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                 'required' : 'required'}))
    course = forms.ModelChoiceField(queryset=Courses.objects.all(),widget=forms.Select(attrs={
                                                                                            'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                            'required' : 'required'}))
    # batch = forms.ChoiceField(choices=BatchChoices.choices,widget=forms.Select(attrs={
    #                                                                                 'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                 'required' : 'required'}))
    batch = forms.ModelChoiceField(queryset=Batches.objects.all(),widget=forms.Select(attrs={
                                                                                            'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                            'required' : 'required'}))
    # trainer_name = forms.ChoiceField(choices=TrainerChoices.choices,widget=forms.Select(attrs={
    #                                                                                 'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                 'required' : 'required'}))
    trainer = forms.ModelChoiceField(queryset=Trainers.objects.all(),widget=forms.Select(attrs={
                                                                                                'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                                'required' : 'required'}))
    
    def clean(self):

        cleaned_data = super().clean()

        pincode = cleaned_data.get('pincode')

        email =cleaned_data.get('email')

        if students.objects.filter(profile__username=email).exists():

            self.add_error('email','email  is already registered. please change email')

        if len(pincode) < 6:

            self.add_error('pincode','pincode must be 6 digits')

        return cleaned_data
    
    def __init__(self,*args,**kwargs):

        super(StudentsRegisterForm,self).__init__(*args,**kwargs)

        if not self.instance:
            
            self.fields.get('photo').widget.attrs['required'] = 'required'

   