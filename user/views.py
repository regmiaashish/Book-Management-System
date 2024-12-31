from django.shortcuts import render,redirect
from user.forms import  RegisterForm
from user.models import UserBalance
from user.forms import UserBalanceForm
from transaction.service import TransactionService
from transaction.models import Transaction
from django.db import transaction

# # Create your views here.
# def register_user(request):
#     form = AuthenticationForm()
#     if request.method == "POST":
#         form = AuthenticationForm(request.POST)
#     info = { "form": form}
#     return render(request, "create/login.html", info)
def create_user(request):
    form = RegisterForm()
    context={
        'data':form
    }
    return render(request,'create/create_user.html',context)






@transaction.atomic
def admin_add_balance(request):
    form = UserBalanceForm()
    if request.method == "POST":
        form = UserBalanceForm(request.POST)
        if form.is_valid():
            form.save()
            TransactionService.create_transaction(
                "Top up",
                request.POST['user'],
                request.POST['balance'],
                Transaction.Transactionstatus.COMPLETED,
                Transaction.PaymentMethod.ADMIN,
            )
            return redirect('/users/userbalance')
    context = {
        'form':form
    }
    return render(request, 'user/balance-create.html',context)


def list_user_balance(request):
    user_balance = UserBalance.objects.all()
    context = {
        'user_balance':user_balance
    }
    return render(request, 'user/balance-list.html',context)