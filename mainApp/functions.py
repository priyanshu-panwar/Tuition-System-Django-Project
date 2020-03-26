from .models import *
from django.core import mail
from datetime import time
import math
import string
import random
import hashlib
from django.core.mail import send_mail

# functions


def contracted_mail_book(student, tutor, bookingDay, bookingTime, bookingEnd):
    message_subject1 = "New Booking"
    message_body1 = "You have been booked by: " + student.user.name + "\nSession Date: " + str(
        bookingDay) + "\nTime: " + str(bookingTime) + "-" + str(bookingEnd)
    mail_from1 = "My Tutors"
    mail_to1 = [str(tutor.user.email)]

    message_subject2 = "Booking Confirmation"
    message_body2 = "Confirmation of booking with: " + tutor.user.name + "\nSession Date: " + str(
        bookingDay) + "\nTime: " + str(bookingTime) + "-" + str(bookingEnd)
    mail_from2 = "My Tutors"
    mail_to2 = [str(student.user.email)]

    send_mail(message_subject1, message_body1, mail_from1,[mail_to1,],fail_silently=False,)
    send_mail(message_subject2, message_body2, mail_from2,[mail_to2,],fail_silently=False,)
    """
    with mail.get_connection() as connection:
        mail.EmailMessage(
            message_subject1, message_body1, mail_from1, [mail_to1],
            connection=connection,
        ).send()
        mail.EmailMessage(
            message_subject2, message_body2, mail_from2, [mail_to2],
            connection=connection,
        ).send()
    """
    return


def private_mail_book(student, tutor, bookingDay, bookingTime, bookingEnd, transaction):
    hour = transaction.time.hour
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    minute = transaction.time.minute
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)

    message_subject1 = "New Booking"
    message_body1 = "You have been booked by: " + student.user.name + "\nSession Date: " + str(
        bookingDay) + "\nTime: " + str(bookingTime) + "-" + str(
        bookingEnd) + "\nFunds that will be added to your wallet after session end: " + str(transaction.amount)
    mail_from1 = "My Tutors"
    mail_to1 = [str(tutor.user.email)]

    message_subject2 = "Booking Confirmation"
    message_body2 = "Confirmation of booking with: " + tutor.user.name + "\nSession Date: " + str(
        bookingDay) + "\nTime: " + str(bookingTime) + "-" + str(
        bookingEnd) + "\nFunds subtracted from your wallet: " + str(transaction.amount) + "\nTransaction ID: " + str(
        transaction.id) + "\nTransaction Date: " + str(transaction.date) + "\nTransaction Time: " + hour + ":" + minute
    mail_from2 = "My Tutors"
    mail_to2 = [str(student.user.email)]

    send_mail(message_subject1, message_body1, mail_from1,[mail_to1,],fail_silently=False,)
    send_mail(message_subject2, message_body2, mail_from2,[mail_to2,],fail_silently=False,)
"""
    with mail.get_connection() as connection:
        mail.EmailMessage(
            message_subject1, message_body1, mail_from1, [mail_to1],
            connection=connection,
        ).send()
        mail.EmailMessage(
            message_subject2, message_body2, mail_from2, [mail_to2],
            connection=connection,
        ).send()
"""


def contracted_mail_cancel(student, tutor, bookingDay, bookingTime, bookingEnd):
    message_subject1 = "Booking Cancelled"
    message_body1 = "Your booking have been cancelled by: " + student.user.name + "\nSession Date: " + str(
        bookingDay) + "\nTime: " + str(bookingTime) + "-" + str(bookingEnd)
    mail_from1 = "My Tutors"
    mail_to1 = [str(tutor.user.email)]

    message_subject2 = "Cancellation Confirmation"
    message_body2 = "Confirmation of cancellation with: " + tutor.user.name + "\nSession Date: " + str(
        bookingDay) + "\nTime: " + str(bookingTime) + "-" + str(bookingEnd)
    mail_from2 = "My Tutors"
    mail_to2 = [str(student.user.email)]
    send_mail(message_subject1, message_body1, mail_from1,[mail_to1,],fail_silently=False,)
    send_mail(message_subject2, message_body2, mail_from2,[mail_to2,],fail_silently=False,)
"""
    with mail.get_connection() as connection:
        mail.EmailMessage(
            message_subject1, message_body1, mail_from1, [mail_to1],
            connection=connection,
        ).send()
        mail.EmailMessage(
            message_subject2, message_body2, mail_from2, [mail_to2],
            connection=connection,
        ).send()
"""


def private_mail_cancel(student, tutor, bookingDay, bookingTime, bookingEnd, transaction):
    message_subject1 = "Booking Cancelled"
    message_body1 = "Your booking have been cancelled by: " + student.user.name + "\nSession Date: " + str(
        bookingDay) + "\nTime: " + str(bookingTime) + "-" + str(bookingEnd)
    mail_from1 = "My Tutors"
    mail_to1 = [str(tutor.user.email)]

    hour = transaction.time.hour
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    minute = transaction.time.minute
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)

    message_subject2 = "Cancellation Confirmation"
    message_body2 = "Confirmation of cancellation with: " + tutor.user.name + "\nSession Date: " + str(
        bookingDay) + "\nTime: " + str(bookingTime) + "-" + str(
        bookingEnd) + "\nFunds added back to your wallet: " + str(transaction.amount) + "\nTransaction ID: " + str(
        transaction.id) + "\nTransaction Date: " + str(transaction.date) + "\nTransaction Time: " + hour + ":" + minute
    mail_from2 = "My Tutors"
    mail_to2 = [str(student.user.email)]
    send_mail(message_subject1, message_body1, mail_from1,[mail_to1,],fail_silently=False,)
    send_mail(message_subject2, message_body2, mail_from2,[mail_to2,],fail_silently=False,)
"""
    with mail.get_connection() as connection:
        mail.EmailMessage(
            message_subject1, message_body1, mail_from1, [mail_to1],
            connection=connection,
        ).send()
        mail.EmailMessage(
            message_subject2, message_body2, mail_from2, [mail_to2],
            connection=connection,
        ).send()
"""


def wallet_mail_add(user, amount, wallet, transaction):
    hour = transaction.time.hour
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    minute = transaction.time.minute
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)

    message_subject = "Wallet Update"
    mail_from = "My Tutors"
    message_body = "Funds added to wallet: " + str(amount) + "\nNew Balance: " + str(
        wallet.balance) + "\nTransactionID: " + str(transaction.id) + "\nTransaction Date: " + str(
        transaction.date) + "\nTransaction Time: " + hour + ":" + minute
    mail_to = [str(user.email)]
    send_mail(message_subject, message_body, mail_from,[mail_to,],fail_silently=False,)
"""
    with mail.get_connection() as connection:
        mail.EmailMessage(
            message_subject, message_body, mail_from, [mail_to],
            connection=connection,
        ).send()
"""


def wallet_mail_subtract(user, amount, wallet, transaction):
    message_subject = "Wallet Update"
    mail_from = "My Tutors"
    hour = transaction.time.hour
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    minute = transaction.time.minute
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    message_body = "Funds subtracted from wallet: " + str(amount) + "\nNew Balance: " + str(
        wallet.balance) + "\nTransactionID: " + str(transaction.id) + "\nTransaction Date: " + str(
        transaction.date) + "\nTransaction Time: " + hour + ":" + minute
    mail_to = [str(user.email)]
    send_mail(message_subject, message_body, mail_from,[mail_to,],fail_silently=False,)
"""
    with mail.get_connection() as connection:
        mail.EmailMessage(
            message_subject, message_body, mail_from, [mail_to],
            connection=connection,
        ).send()
"""


def review_email(booking):
    link = "http://localhost:8000/mainApp/review/" + str(booking.id)
    message_subject = "Submit Review Invitation"
    mail_from = "My Tutors"
    message_body = "This is an invitation to submit a review of the learning session with: " + booking.tutor.user.name + "\nDate: " + str(
        booking.date) + "\nPlease click on the link to submit the review: " + link
    mail_to = [str(booking.student.user.email)]
    send_mail(message_subject, message_body, mail_from,[mail_to,],fail_silently=False,)
"""
    with mail.get_connection() as connection:
        mail.EmailMessage(
            message_subject, message_body, mail_from, [mail_to],
            connection=connection,
        ).send()
"""


def pwd_reset_mail(user, token):
    message_subject1 = "Password Reset Request"
    message_body1 = "Hello! \n You recently requested a password reset for Tutoria. Please visit the link below to reset your password\n"
    message_body1 = message_body1 + "http://localhost:8000/mainApp/resetpwd?token=" + token
    mail_from1 = "My Tutor"
    mail_to1 = [str(user.email)]
    #send_mail(message_subject1, message_body1, mail_from1,[mail_to1,],fail_silently=False,)

    with mail.get_connection() as connection:
        mail.EmailMessage(
            message_subject1, message_body1, mail_from1, [mail_to1],
            connection=connection,
        ).send()



def admin_withdraw_mail(amount, bal):
    message_subject1 = "Money withdrawn from your wallet"
    message_body1 = str(amount) + "HKD were withrawn from MyTutor's wallet. The new balance is " + str(bal)
    mail_from1 = "My Tutors"
    mail_to1 = ["admin@mytutor.com"]
    send_mail(message_subject1, message_body1, mail_from1,[mail_to1,],fail_silently=False,)
"""
    with mail.get_connection() as connection:
        mail.EmailMessage(
            message_subject1, message_body1, mail_from1, [mail_to1],
            connection=connection,
        ).send()
"""


def rateWithCommision(tutorRate):
    return round(tutorRate * 1.05, 2)


def checkUser(uid, request):
    isTutor = False
    isStudent = False
    if 'tid' in request.session:
        isTutor = True
    if 'sid' in request.session:
        isStudent = True
    return isTutor, isStudent


def checkUserFromDB(uid):
    isTutor = Tutor.objects.filter(user=uid).exists()
    isStudent = Student.objects.filter(user=uid).exists()
    return isTutor, isStudent


def isAuthenticated(request):
    if 'uid' not in request.session:
        return False
    else:
        return True


def getTutor(uid):
    return Tutor.objects.get(user=uid)


def getStudent(uid):
    return Student.objects.get(user=uid)


def getPrivateSlots():
    slots = []
    slotsToRender = ["07:00-08:00", "08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00",
                     "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00",
                     "19:00-20:00"]
    for t in slotsToRender:
        slots.append(t.split('-')[0])
    return slots, slotsToRender


def getContractedSlots():
    slots = []
    slotsToRender = ["07:00-07:30", "07:30-08:00", "08:00-08:30", "08:30-09:00", "09:00-09:30", "09:30-10:00",
                     "10:00-10:30", "10:30-11:00", "11:00-11:30", "11:30-12:00", "12:00-12:30", "12:30-13:00",
                     "13:00-13:30", "13:30-14:00", "14:30-15:00", "15:00-15:30", "15:30-16:00", "16:00-16:30",
                     "16:30-17:00", "17:00-17:30", "17:30-18:00", "18:00-18:30", "18:30-19:00"]
    for t in slotsToRender:
        slots.append(t.split('-')[0])
    return slots, slotsToRender


def getWeekdays():
    return ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def getMonths():
    return ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def getQuerySetWeekdays():
    return ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


def checkIfTutorPrivate(tutor):
    return isinstance(tutor, PrivateTutor)


def makeToken(email_address):
    not_hashed = None
    user = None
    if User.objects.filter(email=email_address).exists():
        user = User.objects.get(email=email_address)
        while True:
            not_hashed = ""
            for i in range(8):
                not_hashed = not_hashed + random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            hashed = hashlib.md5(not_hashed.encode('utf-8')).hexdigest()
            if not PasswordToken.objects.filter(token=hashed).exists():
                new_token = PasswordToken(user=user, token=hashed)
            new_token.save()
            break
    return not_hashed, user


def checkToken(token):
    hashed = hashlib.md5(token.encode('utf-8')).hexdigest()
    if not PasswordToken.objects.filter(token=hashed).exists():
        return None, None
    else:
        pwdtkn = PasswordToken.objects.get(token=hashed)
        return User.objects.get(id=pwdtkn.user.id), pwdtkn
