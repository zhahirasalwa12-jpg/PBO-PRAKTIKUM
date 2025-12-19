<<<<<<< HEAD
from abc import ABC, abstractmethod

class ValidatorManagerBefore:
    def validate(self, mahasiswa, matakuliah):
        # Validasi SKS
        if mahasiswa["sks"] + matakuliah["sks"] > 24:
            print("Gagal: SKS melebihi batas")
            return False

        # Validasi Prasyarat
        if matakuliah["prasyarat"] not in mahasiswa["matkul_lulus"]:
            print("Gagal: Prasyarat belum terpenuhi")
            return False

        print("Registrasi berhasil (Before Refactoring)")
        return True

class Validator(ABC):
    @abstractmethod
    def validate(self, mahasiswa, matakuliah) -> bool:
        pass


class SKSValidator(Validator):
    def validate(self, mahasiswa, matakuliah) -> bool:
        if mahasiswa["sks"] + matakuliah["sks"] > 24:
            print("Gagal: SKS melebihi batas")
            return False
        return True


class PrasyaratValidator(Validator):
    def validate(self, mahasiswa, matakuliah) -> bool:
        if matakuliah["prasyarat"] not in mahasiswa["matkul_lulus"]:
            print("Gagal: Prasyarat belum terpenuhi")
            return False
        return True


class ValidatorManager:
    def __init__(self, validators):
        self.validators = validators

    def validate(self, mahasiswa, matakuliah):
        for validator in self.validators:
            if not validator.validate(mahasiswa, matakuliah):
                return False

        print("Registrasi berhasil (After Refactoring)")
        return True

if __name__ == "__main__":

    mahasiswa = {
        "nama": "Andi",
        "sks": 20,
        "matkul_lulus": ["Algoritma", "Basis Data"]
    }

    matakuliah = {
        "nama": "Pemrograman Web",
        "sks": 3,
        "prasyarat": "Basis Data"
    }

    print("=== SEBELUM REFACTORING ===")
    before = ValidatorManagerBefore()
    before.validate(mahasiswa, matakuliah)

    print("\n=== SESUDAH REFACTORING ===")
    validators = [
        SKSValidator(),
        PrasyaratValidator()
    ]

    after = ValidatorManager(validators)
    after.validate(mahasiswa, matakuliah)
=======
from abc import ABC, abstractmethod

class ValidatorManagerBefore:
    def validate(self, mahasiswa, matakuliah):
        # Validasi SKS
        if mahasiswa["sks"] + matakuliah["sks"] > 24:
            print("Gagal: SKS melebihi batas")
            return False

        # Validasi Prasyarat
        if matakuliah["prasyarat"] not in mahasiswa["matkul_lulus"]:
            print("Gagal: Prasyarat belum terpenuhi")
            return False

        print("Registrasi berhasil (Before Refactoring)")
        return True

class Validator(ABC):
    @abstractmethod
    def validate(self, mahasiswa, matakuliah) -> bool:
        pass


class SKSValidator(Validator):
    def validate(self, mahasiswa, matakuliah) -> bool:
        if mahasiswa["sks"] + matakuliah["sks"] > 24:
            print("Gagal: SKS melebihi batas")
            return False
        return True


class PrasyaratValidator(Validator):
    def validate(self, mahasiswa, matakuliah) -> bool:
        if matakuliah["prasyarat"] not in mahasiswa["matkul_lulus"]:
            print("Gagal: Prasyarat belum terpenuhi")
            return False
        return True


class ValidatorManager:
    def __init__(self, validators):
        self.validators = validators

    def validate(self, mahasiswa, matakuliah):
        for validator in self.validators:
            if not validator.validate(mahasiswa, matakuliah):
                return False

        print("Registrasi berhasil (After Refactoring)")
        return True

if __name__ == "__main__":

    mahasiswa = {
        "nama": "Andi",
        "sks": 20,
        "matkul_lulus": ["Algoritma", "Basis Data"]
    }

    matakuliah = {
        "nama": "Pemrograman Web",
        "sks": 3,
        "prasyarat": "Basis Data"
    }

    print("=== SEBELUM REFACTORING ===")
    before = ValidatorManagerBefore()
    before.validate(mahasiswa, matakuliah)

    print("\n=== SESUDAH REFACTORING ===")
    validators = [
        SKSValidator(),
        PrasyaratValidator()
    ]

    after = ValidatorManager(validators)
    after.validate(mahasiswa, matakuliah)
>>>>>>> 62723ba572f986321ceb1f39bc4fb779b6dc725a
