import { Controller } from "stimulus";

export default class extends Controller {

    connect() {
        console.log("Hello from dummy")
    }

    disconnect() {
        console.log("Bye from dummy")
    }
}
