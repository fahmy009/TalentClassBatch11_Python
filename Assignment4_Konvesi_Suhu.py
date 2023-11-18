nilai_input = float(
    input("Input Suhu : ")
)  # input menggunakan function input dari python


def celcius_ke_farenheit(suhu):  # Function Konversi Celcius ke Farenheit
    return 9 / 5 * (suhu + 32)  # Hasil akan di return langsung


def celcius_ke_kelvin(suhu):  # Function Konversi Celcius ke Kelvin
    return suhu + 273.15  # Hasil akan di return langsung


def kelvin_ke_celcius(suhu):  # Function Konversi Kelvin ke Celcius
    return suhu - 273.15  # Hasil akan di return langsung


def kelvin_ke_farenheit(suhu):  # Function Konversi Kelvin ke Farenheit
    return 9 / 5 * (suhu - 273.15) + 32  # Hasil akan di return langsung


def farenheit_ke_kelvin(suhu):  # Function Konversi Farenheit ke Kelvin
    return 5 / 9 * (suhu - 32) + 273  # Hasil akan di return langsung


def farenheit_ke_celcius(suhu):  # Function Konversi Farenheit ke Celcius
    return 5 / 9 * (suhu - 32)  # Hasil akan di return langsung


if nilai_input <= 100:  # Kondisi jika nilai input antara 0 - 100 dinyatakan Celcius
    print(f"Jenis Suhu Yang Diinput adalah Celcius dengan {nilai_input} Derajat")
    print(f"---------------------------------------------------------------")
    print(f"Suhu akan di konversi ke Kelvin dan Farenheit")
    print(f"---------------------------------------------------------------")
    print(
        f"Suhu hasil konversi ke Kelvin adalah {float(celcius_ke_kelvin(nilai_input)):.2f} K"
    )
    print(f"---------------------------------------------------------------")
    print(
        f"Suhu hasil konversi ke Farenheit adalah {float(celcius_ke_farenheit(nilai_input)):.2f} F"
    )
elif (
    nilai_input >= 273 and nilai_input <= 373
):  # Kondisi jika nilai input antara 273 - 373 dinyatakan Kelvin
    print(f"Jenis Suhu Yang Diinput adalah Kelvin dengan {nilai_input} Derajat")
    print(f"---------------------------------------------------------------")
    print(f"Suhu akan di konversi ke Celcius dan Farenheit")
    print(f"---------------------------------------------------------------")
    print(
        f"Suhu hasil konversi ke Celcius adalah {float(kelvin_ke_celcius(nilai_input)):.2f} C"
    )
    print(f"---------------------------------------------------------------")
    print(
        f"Suhu hasil konversi ke Farenheit adalah {float(kelvin_ke_farenheit(nilai_input)):.2f} F"
    )
else:  # Kondisi jika nilai input antara 100 - 273 dinyatakan Farenheit
    print(f"Jenis Suhu Yang Diinput adalah Farenheit dengan {nilai_input} Derajat")
    print(f"---------------------------------------------------------------")
    print(f"Suhu akan di konversi ke Celcius dan Kelvin")
    print(f"---------------------------------------------------------------")
    print(
        f"Suhu hasil konversi ke Celcius adalah {float(farenheit_ke_celcius(nilai_input)):.2f} C"
    )
    print(f"---------------------------------------------------------------")
    print(
        f"Suhu hasil konversi ke Kelvin adalah {float((farenheit_ke_kelvin(nilai_input))):.2f} F"
    )
