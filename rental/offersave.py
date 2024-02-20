from rental.models import Offer
offer = Offer(text='A cozy space in "loft" style.\nPerfect for young couples')
offer.save()
offer = Offer(text='A warm house for a big family')
offer.save()