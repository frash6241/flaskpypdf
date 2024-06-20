-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-06-2024 a las 02:49:17
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `diario_bd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_estudio`
--

CREATE TABLE `datos_estudio` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `fecha_na` date NOT NULL,
  `sexo` varchar(20) NOT NULL,
  `edad` varchar(10) NOT NULL,
  `peso` varchar(10) NOT NULL,
  `altura` varchar(10) NOT NULL,
  `tel` varchar(10) NOT NULL,
  `cel` varchar(10) NOT NULL,
  `obra_s` varchar(100) NOT NULL,
  `numero_a` varchar(100) NOT NULL,
  `tipo_p` varchar(50) NOT NULL,
  `capacidad_e` varchar(50) NOT NULL,
  `fecha_e` date NOT NULL,
  `medico_o` text NOT NULL,
  `medico_d` text NOT NULL,
  `protocolo` text NOT NULL,
  `observaciones` varchar(100) NOT NULL,
  `motivo_e` text NOT NULL,
  `antecedentes` varchar(200) NOT NULL,
  `factores_r` text NOT NULL,
  `ecg` varchar(50) NOT NULL,
  `eco` varchar(50) NOT NULL,
  `septum` varchar(50) NOT NULL,
  `pared_p` varchar(50) NOT NULL,
  `dfd` varchar(50) NOT NULL,
  `dfs` varchar(50) NOT NULL,
  `imvi` varchar(50) NOT NULL,
  `habitual` varchar(50) NOT NULL,
  `terapia` varchar(50) NOT NULL,
  `minutos` varchar(50) NOT NULL,
  `carga` varchar(50) NOT NULL,
  `prueba_b` varchar(50) NOT NULL,
  `fcmp` varchar(10) NOT NULL,
  `fcmp_porcentaje` varchar(10) NOT NULL,
  `vfcb` varchar(10) NOT NULL,
  `vfcmax` varchar(20) NOT NULL,
  `rcd` varchar(10) NOT NULL,
  `alt_ecg` varchar(20) NOT NULL,
  `isquemia` varchar(20) NOT NULL,
  `test_ad` varchar(10) NOT NULL,
  `motivo` varchar(50) NOT NULL,
  `tiempo_i` varchar(100) NOT NULL,
  `diagnostico` text NOT NULL,
  `conclusiones` text NOT NULL,
  `file` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_estudio`
--

INSERT INTO `datos_estudio` (`id`, `nombre`, `fecha_na`, `sexo`, `edad`, `peso`, `altura`, `tel`, `cel`, `obra_s`, `numero_a`, `tipo_p`, `capacidad_e`, `fecha_e`, `medico_o`, `medico_d`, `protocolo`, `observaciones`, `motivo_e`, `antecedentes`, `factores_r`, `ecg`, `eco`, `septum`, `pared_p`, `dfd`, `dfs`, `imvi`, `habitual`, `terapia`, `minutos`, `carga`, `prueba_b`, `fcmp`, `fcmp_porcentaje`, `vfcb`, `vfcmax`, `rcd`, `alt_ecg`, `isquemia`, `test_ad`, `motivo`, `tiempo_i`, `diagnostico`, `conclusiones`, `file`) VALUES
(29, 'SEGUETTI, EDUARDO mmmmmmm', '1942-01-22', 'masculino', '81 Años   ', '100 [Kg]  ', '179 [cm] ', '/   ', '1145*10383', 'PAMI   ', '', 'Ambulatorio ', 'BUENA ', '2023-08-07', 'SAAD ARIEL KARIM  ', 'MONTEROS  ARIEL ', 'Ejercicio 3 etapas ', '', 'Diagnóstico ', 'Sin antecedentes ', 'HTA, Obeso, Sedentario, Stress ', '', '', '0 [mm]   ', '0 [mm]   ', '0 [mm]   ', '0 [mm]   ', '0 [g] ', 'Antiarrítmicos ', 'Nitratos, Beta Bloqueantes (Suspendido Hs 36) ', '0 [min]   ', '1 METS (0 [Kgm]) ', 'No', '139 LPM ', '53 % ', '0 [cm/s]  ', '#VFCMax#    ', '0 ', 'Sin Alteraciones ', '', 'No ', '', '', 'PACIENTE DE 81 AÑOS  QUE REALIZA TEST DE EVALUACION DIAGNOSTICA  POR DISNEA DE ESFUERZO.  SIN ANTECEDENTES CORONARIOS. DATOS POSITIVOS: HTA, EX TBQ. EN EL ECOBASAL:  VI DE DIAMETROS  LEVEMENTE DILATADOS PARA LA SUPERFICIE CORPORAL.  MOTILIDAD SEPTAL ANOMALA. HIPOQUINESIA GLOBAL.   FUNCION SISTOLICA GLOBAL DEPRIMIDA EN GRADO MODERADO. FEY: 41% (METODO SEMIAUTOMATICO BIPLANO).   MARCADA DILATACION DE AURICULA IZQUIERDA (VOL   67   ML/M2).  POR DOPPLER: PATRON DE  LLENADO PSEUDONORMAL.  ESTENOSIS AORTICA GRAVE (0.7 CM2, GRAD MEDIO: 43  mmHg).  INSUFICIENCIA MITRAL LEVE. INSUFICIENCIA TRICUSPIDEA LEVE QUE PERMITE ESTIMAR UNA PSAP DE 32 mmHg. LINEAS B PULMONARES BILATERES AUMENTADAS DE MANERA SIGNIFICATIVA (>10). NO SE REALIZO EJERCICIO POR CONSIDERARSE ESTENOSIS AORTICA  GRAVE SINTOMATICA POR DISNEA.      ', 'Prueba Negativa PRUEBA DE APREMIO SUSPENDIDA EN ETAPA BASAL POR ESTENOSIS AORTICA GRAVE SINTOMATICA. ECO Estrés es un producto de Eccosur - www.eccosur.com ECO Estrés Informe - 07/08/2023 - Paciente: SEGUETTI, EDUARDO - Página 1 de ', '00210600 13890SEGUETTI_EDUARDO_ECO_Estrés_Informe_07_08_2023.pdf');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datos_estudio`
--
ALTER TABLE `datos_estudio`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datos_estudio`
--
ALTER TABLE `datos_estudio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
