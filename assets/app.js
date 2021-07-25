// Cargar styles
import "./style.scss";

// Cargar componentes de stimulus
import "@materializecss/materialize"
import { Application } from "stimulus"
import { definitionsFromContext } from "stimulus/webpack-helpers"


const application = Application.start()
const app_context = require.context("./controllers", true, /\.js$/)
application.load(definitionsFromContext(app_context))
