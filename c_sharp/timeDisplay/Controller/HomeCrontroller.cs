using Microsoft.AspNetCore.Mvc;
namespace timeDisplay
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public ViewResult Index()
        {
            return View("Index");
        }
    }
}