################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Src/Boilerplate/stm32f7xx_hal_msp.c \
../Core/Src/Boilerplate/stm32f7xx_it.c \
../Core/Src/Boilerplate/syscalls.c \
../Core/Src/Boilerplate/sysmem.c \
../Core/Src/Boilerplate/system_stm32f7xx.c 

OBJS += \
./Core/Src/Boilerplate/stm32f7xx_hal_msp.o \
./Core/Src/Boilerplate/stm32f7xx_it.o \
./Core/Src/Boilerplate/syscalls.o \
./Core/Src/Boilerplate/sysmem.o \
./Core/Src/Boilerplate/system_stm32f7xx.o 

C_DEPS += \
./Core/Src/Boilerplate/stm32f7xx_hal_msp.d \
./Core/Src/Boilerplate/stm32f7xx_it.d \
./Core/Src/Boilerplate/syscalls.d \
./Core/Src/Boilerplate/sysmem.d \
./Core/Src/Boilerplate/system_stm32f7xx.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/Boilerplate/%.o Core/Src/Boilerplate/%.su Core/Src/Boilerplate/%.cyclo: ../Core/Src/Boilerplate/%.c Core/Src/Boilerplate/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F756xx -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src-2f-Boilerplate

clean-Core-2f-Src-2f-Boilerplate:
	-$(RM) ./Core/Src/Boilerplate/stm32f7xx_hal_msp.cyclo ./Core/Src/Boilerplate/stm32f7xx_hal_msp.d ./Core/Src/Boilerplate/stm32f7xx_hal_msp.o ./Core/Src/Boilerplate/stm32f7xx_hal_msp.su ./Core/Src/Boilerplate/stm32f7xx_it.cyclo ./Core/Src/Boilerplate/stm32f7xx_it.d ./Core/Src/Boilerplate/stm32f7xx_it.o ./Core/Src/Boilerplate/stm32f7xx_it.su ./Core/Src/Boilerplate/syscalls.cyclo ./Core/Src/Boilerplate/syscalls.d ./Core/Src/Boilerplate/syscalls.o ./Core/Src/Boilerplate/syscalls.su ./Core/Src/Boilerplate/sysmem.cyclo ./Core/Src/Boilerplate/sysmem.d ./Core/Src/Boilerplate/sysmem.o ./Core/Src/Boilerplate/sysmem.su ./Core/Src/Boilerplate/system_stm32f7xx.cyclo ./Core/Src/Boilerplate/system_stm32f7xx.d ./Core/Src/Boilerplate/system_stm32f7xx.o ./Core/Src/Boilerplate/system_stm32f7xx.su

.PHONY: clean-Core-2f-Src-2f-Boilerplate

