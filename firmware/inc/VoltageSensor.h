/*
 * VoltageSensor.h
 *
 *  Created on: Mar 18, 2024
 *      Author: Rivindu Ranasinghe
 */

#ifndef INC_CURRENTADC_H_
#define INC_CURRENTADC_H_

#include "main.h"
#include "adc.h"
#include "dma.h"

#define WINDOW_SIZE 150

#define NO_ADCs 2

extern uint32_t adcBuffer[NO_ADCs]; // Start_ADC_DMA in dma.c

extern int taskCompletedFlag; //used inside the HAL_ADC_ConvCpltCallback function in adc.c





void movingAvgCalculation();
void handleTaskCompletion();
void performCalculation();



#endif /* INC_CURRENTADC_H_ */
