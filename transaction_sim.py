
data = {
	"ID":
	{
		"I00000000000000000001":
		{
			"key": "0z8YmIROEn9tMCMnyjzOI",
			"transactions":
			{
				#For testing
				0:
				{
					"from": "I00000000000000000003", #Sent from someone else
					"amount": 50
				}
			}
		},

		"I00000000000000000002":
		{
			"key": "0Yr8QJBD4iui9aZV7NsxR",
			"transactions":
			{

			}
		}	
	}
}


def get_balance_data(ID):
	
	total_balance = 0

	for transaction_data in data["ID"][ID]["transactions"].values():
		
		try:
			transaction_data["to"]
			total_balance -= transaction_data["amount"]
			
		except KeyError:

			if transaction_data["from"]:
				total_balance += transaction_data["amount"]

	return total_balance


def get_transaction_data(ID):

	return data["ID"][ID]["transactions"]


def get_transaction_id(ID):

	return len(data["ID"][ID]["transactions"])


def new_transaction(p, ID, amount):

	if p == "sender":
		return {"to": ID, "amount": amount}
	elif p == "receiver":
		return {"from": ID, "amount": amount}


class Sender:

	priv_key: str

	def __init__(self, senderID: str):

		self.senderID = senderID


	def send(self, receiverID, amount):

		try:
			if data["ID"][self.senderID]["key"] == self.priv_key:
				
				if amount > 0:

					if get_balance_data(self.senderID) >= amount:

						try:
							sender_transaction_id   = get_transaction_id(self.senderID)
							receiver_transaction_id = get_transaction_id(receiverID)

							sender_new_transaction   = new_transaction("sender", receiverID, amount)
							receiver_new_transaction = new_transaction("receiver", self.senderID, amount)

							data["ID"][self.senderID]["transactions"].update({sender_transaction_id: sender_new_transaction})
							data["ID"][receiverID]["transactions"].update({receiver_transaction_id: receiver_new_transaction})

							print("Transaction successful.")

						except KeyError:

							print(f"Sending Failed: ID {receiverID} does not exist.")
					else:
						print(f"Sending Failed: Unsufficient balance: {get_balance_data(self.senderID)}")
				else:
					print("Sending Failed: Amount must be greater than zero.")
			else:
				print(f"Sending Failed: Key {self.priv_key} is wrong.")

		except KeyError:

			print(f"Sending Failed: ID {self.senderID} does not exist.")


print(f"""
Sender transaction data before sending:      {get_transaction_data("I00000000000000000001")}
Receiver transaction data before receiving:  {get_transaction_data("I00000000000000000002")}

Sender balance data before sending:          {get_balance_data("I00000000000000000001")}
Receiver balance data before receiving:      {get_balance_data("I00000000000000000002")}
""")


sender = Sender("I00000000000000000001")  #SenderID

sender.priv_key = "0z8YmIROEn9tMCMnyjzOI" #SenderKey

sender.send("I00000000000000000002", 10)  #ReceverID, amount


print(f"""
Sender transaction data after sending:       {get_transaction_data("I00000000000000000001")}
Receiver transaction data after receiving:   {get_transaction_data("I00000000000000000002")}

Sender balance data after sending:           {get_balance_data("I00000000000000000001")}
Receiver balance data after receiving:       {get_balance_data("I00000000000000000002")}
""")
