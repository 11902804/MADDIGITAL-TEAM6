import { Color } from "./color.model";

export class Emotion {
    name: string;
    colors: Array<Color>;

    constructor() {
        this.colors = [];
    }
}