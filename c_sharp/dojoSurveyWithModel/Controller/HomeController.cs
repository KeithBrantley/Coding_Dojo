using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using dojoSurveyWithModel.Models;

namespace dojoSurveyWithModel.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public ViewResult Index()
        {
            return View("Index");
        }

        [HttpPost("survey")]
        public ViewResult Submission(Survey yourSurvey)
        {
            return View("survey", yourSurvey);
        }
    }
}