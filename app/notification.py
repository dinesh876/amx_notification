from db.config import Session
from db.models import DeviceUsagesThresholdStatus


def notification(data,percentage):
    session = Session()
    n = DeviceUsagesThresholdStatus(
        user_id= data["userId"], 
        user_uuid = data["userUuid"],
        owner_uuid = data["ownerUuid"],
        type =data["type"],
        code = data["code"],
        message = data["message"],
        timestamp = data["timestamp"],
        action = data["action"],
        poll_delivery_type = data["pollDeliveryType"],
        message_uuid = data["messageUuid"],
        user_identifier = data["userIdentifier"],
        notification_url = data["notificationUrl"],
        notificationa_uthtoken = data["notificationAuthToken"],
        user_purchase_id = data["userPurchaseId"],
        type_entry_id = data["typeEntryId"],
        imsi = data["imsi"],
        msisdn = data["msisdn"],
        iccid = data["iccid"],
        device_usages_threshold = percentage
        )
    
    session.add(n)
    session.commit()