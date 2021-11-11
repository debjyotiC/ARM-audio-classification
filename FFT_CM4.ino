#include <arm_math.h>

const int WINDOW_SIZE = 256;
const int STEP_SIZE = 128;

uint32_t ifftFlag = 0;
uint32_t doBitReverse = 1;

float32_t input_f32[WINDOW_SIZE*2];
float32_t fft_mag_f32[WINDOW_SIZE/2];

arm_cfft_radix4_instance_f32 S_f32;


void setup() {
  Serial.begin(9600);

  for (int i = 0; i < WINDOW_SIZE; i++) {
    input_f32[i] = sin((2 * PI * 400) / 16000 * i);
    Serial.println(input_f32[i]);
  }
  arm_cfft_radix4_init_f32(&S_f32, WINDOW_SIZE, ifftFlag, doBitReverse);
}

void loop() {
  // FFT calculation
  arm_cfft_radix4_f32(&S_f32, input_f32);
  arm_cmplx_mag_f32(input_f32, fft_mag_f32,  WINDOW_SIZE/2);

  for(int i = 0; i < WINDOW_SIZE/2; i++){
    //Serial.println(fft_mag_f32[i]);
  }
  while(1);
}
