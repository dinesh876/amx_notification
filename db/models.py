from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,TIMESTAMP


Base = declarative_base()

class DeviceUsagesThresholdStatus(Base):
    """
     CREATE TABLE `device_usages_threshold_status` (
     `ID` int NOT NULL AUTO_INCREMENT,
     `USER_ID` varchar(16) DEFAULT NULL,
     `USER_UUID` varchar(256) DEFAULT NULL,
     `OWNER_UUID` varchar(256) DEFAULT NULL,
     `TYPE` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
     `CODE` varchar(56) DEFAULT NULL,
     `MESSAGE` varchar(2056) DEFAULT NULL,
     `TIMESTAMP` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
     `ACTION` varchar(16) DEFAULT NULL,
     `POLL_DELIVERY_TYPE` varchar(16) DEFAULT NULL,
     `MESSAGE_UUID` varchar(256) DEFAULT NULL,
     `USER_IDENTIFIER` varchar(256) DEFAULT NULL,
     `NOTIFICATION_URL` varchar(256) DEFAULT NULL,
     `NOTIFICATIONA_UTHTOKEN` varchar(56) DEFAULT NULL,
     `USER_PURCHASE_ID` varchar(56) DEFAULT NULL,
     `TYPE_ENTRY_ID` varchar(56) DEFAULT NULL,
     `IMSI` varchar(56) NOT NULL DEFAULT '0',
     `MSISDN` varchar(56) NOT NULL DEFAULT '0',
     `ICCID` varchar(56) NOT NULL DEFAULT '0',
     `DEVICE_USAGES_THRESHOLD` varchar(56) DEFAULT NULL,
     `IS_DELETED` tinyint(1) DEFAULT '0',
     `DELETED_DATE` datetime DEFAULT NULL,
     PRIMARY KEY (`ID`),
     KEY `IMSI` (`IMSI`),
     KEY `MSISDN` (`MSISDN`),
     KEY `ICCID` (`ICCID`)
     ) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
    """ 

    __tablename__ = "device_usages_threshold_status"

    id = Column(Integer,primary_key=True)
    user_id = Column(String(16))
    user_uuid = Column(String(256))
    owner_uuid = Column(String(256))
    type = Column(String(256))
    code = Column(String(56))
    message = Column(String(2056))
    timestamp = Column(TIMESTAMP,nullable=False)
    action = Column(String(16))
    poll_delivery_type = Column(String(16))
    message_uuid = Column(String(256))
    user_identifier = Column(String(256))
    notification_url = Column(String(256))
    notificationa_uthtoken = Column(String(56))
    user_purchase_id = Column(String(56))
    type_entry_id = Column(String(56))
    imsi = Column(String(56),nullable=False)
    msisdn = Column(String(56),nullable=False)
    iccid = Column(String(56),nullable=False)
    device_usages_threshold = Column(String(56))
    is_deleted = Column(Integer,default=0)
    deleted_date = Column(TIMESTAMP)