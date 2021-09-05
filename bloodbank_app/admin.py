from django.contrib import admin

from .models import Register
admin.site.register(Register)

from .models import PaymentGateway
admin.site.register(PaymentGateway)

from .models import Donation
admin.site.register(Donation)

from .models import Contact
admin.site.register(Contact)

from .models import DonorRegister
admin.site.register(DonorRegister)

#from .models import login
#admin.site.register(login)





