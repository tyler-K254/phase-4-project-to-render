
from app import app
from models import db, Car
# from dotenv import dotenv_values

# db.init_app(app)

with app.app_context():

    print('Deleting existing cars...')
    Car.query.delete()

    print('Creating car objects...')
    Mercedes = Car(
        name='Mercedies Benz',
        model='S550 LWB',
        image='https://aristocars.co.ke/wp-content/uploads/2021/12/WhatsApp-Image-2021-10-28-at-7.41.51-PM.jpeg' 
    )
    Ford = Car(
        name='Ford',
        model='Ford Ranger[F-150]',
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaw5_j_0FXJuvSok8pYCEg8t8B3RSDbLosKJqZ2rLF&s"
        )
    Subaru = Car(
        name='Subaru',
        model='Impreza 22B',
        image='https://hips.hearstapps.com/hmg-prod/images/subaru-22-b-front-6419cd0ac4059.png?crop=1.00xw:0.851xh;0,0.108xh&resize=980:*'
    )
    Nissan = Car(
        name='Nissan',
        model='240SX',
        image='https://www.carscoops.com/wp-content/uploads/2022/01/Nissan-Silvia-240-SX-r1-1024x555.jpg'
    )
    Ford2 = Car(
        name='Ford Mustang',
        model='Shelby GT500',
        image='https://cdn.motor1.com/images/mgl/Gx4J1/s3/2022-ford-mustang-shelby-gt500-heritage-edition-front-corner-high-angle.webp'
        )
    Honda = Car(
        name='Honda',
        model='Civic Type R',
        image='https://www.honda.ca/-/media/Brands/Honda/Models/TYPE-R/2023/Overview/03_Key-Features/Honda_Civic_TypeR_key-features_desktop_1036x520.png?h=520&iar=0&w=1036&rev=86a8e32265ac446dadf66e704156f39f&hash=F79E92877AED80EC7864F74CC77B2267'
    )
    volkswagen = Car(
        name='volkswagen',
        model='golf mk7',
        image='https://media.autoexpress.co.uk/image/private/s--X-WVjvBW--/f_auto,t_content-image-full-desktop@1/v1562255566/autoexpress/vw-golf-mk7-uk-1.jpg'
    )
    Nissan2 = Car(
        name='Nissan',
        model='Altima 2020',
        image='https://hips.hearstapps.com/hmg-prod/images/2023-nissan-altima-113-1654783718.jpg?crop=0.712xw:0.535xh;0.132xw,0.347xh&resize=1200:*'
    )

    Hyundai = Car(
        name='Hyundai',
        model='Sonata 2023',
        image='https://s7d1.scene7.com/is/image/hyundai/2022-sonata-1?wid=1200&hei=630&qlt=85,0&fmt=webp'
    )

    Jeep = Car(
        name='Jeep',
        model='Wrangler 2023',
        image='https://media.ed.edmunds-media.com/jeep/wrangler/2023/oem/2023_jeep_wrangler_convertible-suv_high-tide_fq_oem_1_1600.jpg'
    )

    print('Adding Car objects to transaction...')
    db.session.add_all([Mercedes, Ford, Ford2, Subaru, Nissan, Honda, volkswagen, Nissan2, Hyundai, Jeep])
    print('Committing transaction...')
    db.session.commit()
    print('Complete.')