// readthedocs: https://developers.meethue.com/develop/hue-api/lights-api/ 
// Turn light on/ off, change hue and effects: PUT /api/<username>/lights/<id>/state

export class Light {
    id: string;
    on: boolean; // light on/off
    bri: number; //brightness, min:1 max:254
    hue: number; //color, wrapping value 0-65535. Red:0, 65535 | Green: 25500 | Blue: 46920
    sat: number; //saturation, min:0 (white) max:254 (colored)
    ct: number; // The Mired color temperature of the light. 2012 connected lights are capable of 153 (6500K) to 500 (2000K).
    alert: string; //readthedocs
    effect: string; //The dynamic effect of the light. Currently “none” and “colorloop” are supported. Other values will generate an error of type 7.Setting the effect to colorloop will cycle through all hues using the current brightness and saturation settings.
    transitiontime: number; //The duration of the transition from the light’s current state to the new state. This is given as a multiple of 100ms and defaults to 4 (400ms). For example, setting transitiontime:10 will make the transition last 1 second.
    bri_inc: number; //readthedocs
    sat_inc: number; //readthedocs
    hue_inc: number; //Increments or decrements the value of the hue. hue_inc is ignored if the hue attribute is provided. Any ongoing color transition is stopped. Setting a value of 0 also stops any ongoing transition. The bridge will return the hue value after the increment is performed. Note if the resulting values are < 0 or > 65535 the result is wrapped. For example:
    /*
    {"hue_inc":  1}
    on a hue value of 65535 results in a hue of 0.
    
    {"hue_inc":  -2}
    on a hue value of 0 results in a hue of 65534.
    */
   ct_inc: number; //readthedocs
   xy_inc: number; //readthedocs

   constructor() {}
}