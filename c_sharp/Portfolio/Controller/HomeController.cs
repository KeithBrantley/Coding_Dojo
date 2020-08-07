using Microsoft.AspNetCore.Mvc;
namespace Portfolio
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public ViewResult Index()
        {
            return View("Index");
        }

        [HttpGet("projects")]
        public ViewResult Projects()
        {
            return View("projects");
        }

        [HttpGet("contact")]
        public ViewResult Contact()
        {
            return View("contact");
        }
    }
}