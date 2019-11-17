from django import forms
from .models import Ficha


class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = [
            'Nombre',
            'DNI',
            'Edad',
            'Tiempo_de_enfermedad',
            # 'Retinopatia',
            # 'Netropatia',
            # 'Hipoglicemia',
            # 'Coma_diabetico',
            # 'Accidente_cerebro_vascular',
            # 'Infarto_miocardio',
            # 'Hipertension',
            # 'Adormecimiento_o_dolor',
            # 'Claudicacion',
            # 'Callos_o_deformidad',
            # 'Sensibilidad_tactil_alterada',
            # 'Sensibilidad_vibratoria_alterada',
            'Sensibilidad_neurovegetativa_alterada',
            # 'Presion_arterial_tobillo',
            # 'Presion_arterial_brazo',
            # 'Recuperacion_termica_a_0_minutos',
            # 'Recuperacion_termica_a_4_minutos',
            # 'Recuperacion_termica_a_8_minutos',
            # 'Presion_plantar_alta',
            # 'Callos',
            # 'Localización',
            # 'Deformidad_del_antepie',
            # 'Tipo_deformidad_del_antepie',
            # 'Deformidad_del_mediopie',
            # 'Lado_afectado',
            # 'Numero',
            # 'Localizacion_1',
            # 'Localizacion_2',
            # 'Localizacion_3',
            # 'Secrecion_1',
            # 'Secrecion_2',
            # 'Color_1',
            # 'Color_predominante',
            # 'Dimensiones_largo_maximo',
            # 'Dimensiones_ancho_maximo',
            # 'Area_de_la_ulcera',
            # 'Fotografia_convencional',
            # 'Zona_de_contaminacion_bacterial',
            # 'Fotografia_autoluminiscente',
            # 'Edema_local',
            # 'Induracion',
            # 'Celulitis_menor_de_2_cm',
            # 'Sensibilidad_o_dolor',
            # 'Secrecion_purulenta',
            # 'Diferencial_termico_alterado',
            # 'Adjuntar_imagen_termica',
            # 'Celulitis_mayor_de_2_cm',
            # 'Absceso',
            # 'Fascitis',
            # 'Artritis_septica',
            # 'Osteomielitis',
            # 'Temperatura_mayor_a_38_o_menor_a_36',
            # 'Frecuencia_cardiaca_mayor_a_90_por_minuto',
            # 'Frecuencia_respiratoria_mayor_a_32_por_minuto',
            # 'Presion_parcial_de_dioxido_de_carbono_menor_de_35_mm_Hg',
            # 'Recuento_celular_mayor_a_12000_o_menor_a_4000',
        ]