import  hashlib
import datetime

class medicalLeaveSystem:
    def __init__(self):
        self.doctor_info = ['101','102','103','104','105','106','107','108','109','110']
        self.blockchain = {}


    def doctorEnd(self):
        print("Please enter doctor.ID for verification")
        docId = input()
        if docId in self.doctor_info:
            print("Enter certificate no.")
            cNo = input()
            print("Enter student ID")
            sId = input()
            print("Enter college ID")
            collegeId = input()
            ml = docId + cNo + sId + collegeId
            str = hashlib.sha256(ml.encode())
            mlHash = str.hexdigest()
            timeStamp = datetime.date.today()
            self.blockchain[mlHash] = timeStamp
            print(self.blockchain)
        else:
            print("Verification failed")


    def universityEnd(self):
        print("Please enter the doctor ID")
        docId = input()
        print("Enter the certificate no.")
        cNo = input()
        print("Enter the studentId")
        sId = input()
        print("Enter the collegeID")
        collegeId = input()
        ml = docId + cNo + sId + collegeId
        str = hashlib.sha256(ml.encode())
        mlHash = str.hexdigest()
        if mlHash in self.blockchain:
            print(self.blockchain[mlHash])
            print("ML Approved")
        else:
            print("Fake ML!!! call the student for enquiry")


if __name__=='__main__':
    temp = medicalLeaveSystem()
    temp.doctorEnd()
    temp.universityEnd()
