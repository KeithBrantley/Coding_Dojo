using Microsoft.AspNetCore.Mvc;
namespace RazorFun
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