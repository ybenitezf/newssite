import { MDCRipple } from '@material/ripple/index';
import { Controller } from "stimulus";

export default class extends Controller {

    connect() {
        this.button = new MDCRipple(this.element);
    }

    disconnect() {
        if ( this.button ) {
            this.button.destroy();
        }
    }
}
