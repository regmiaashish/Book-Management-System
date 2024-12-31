from transaction.models import Transaction
import uuid
from django.contrib.auth.models import User

class TransactionService:
    def create_transaction(txn_name,user,amount,status,payment_method,remarks=None):
        user_data = User.objects.get(id=user)
        txn = Transaction.objects.create(
            name = txn_name,
            amount = amount,
            user = user_data,
            transaction_id =uuid.uuid4(),
            status = status,
            payment_method = payment_method,
            remarks=remarks
        )
        return txn