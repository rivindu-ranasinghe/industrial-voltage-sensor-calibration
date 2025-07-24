/*
 * VoltageSensor.c
 *
 *  Created on: Mar 18, 2024
 *      Author: Rivindu Ranasinghe
 */


#include "main.h"
#include "VoltageSensor.h"
#include "adc.h"
#include "dma.h"



uint32_t adcBuffer	[NO_ADCs]; // Start_ADC_DMA in dma.c

uint32_t adcReadings[NO_ADCs];


int taskCompletedFlag = 0;

int 		sigmaADC	[NO_ADCs];
int 		sampleCount 	= 0;


double pVoltage_Value = 0;





void handleTaskCompletion() {
    if (taskCompletedFlag) {
        // Call the function when the flag is set

        movingAvgCalculation();
        performCalculation();

        // Reset the flag
        taskCompletedFlag = 0;
    }
}


void movingAvgCalculation()
{
	if(sampleCount < WINDOW_SIZE)
	{
		for( int i = 0 ; i < NO_ADCs ; i++ )
		{
			sigmaADC[i] += adcBuffer[i];
		}
		sampleCount++;
	}
	else
	{
		sampleCount = 0;
		for( int i = 0 ; i < NO_ADCs ; i++ )
		{
			adcReadings[i] = sigmaADC[i]/WINDOW_SIZE;
			sigmaADC[i] = 0;


		}

	}
}

void performCalculation() {


	pVoltage_Value = 0.31812062 * adcReadings[1] + 20.75940281;


    //y = a * x + b

}


