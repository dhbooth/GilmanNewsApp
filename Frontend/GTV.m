//
//  GTV.m
//  The Gilman News 5.0
//
//  Created by Davis Booth on 9/9/16.
//  Copyright © 2016 Davis Booth. All rights reserved.
//

#import "GTV.h"

@interface GTV ()

@end

@implementation GTV

- (void)viewDidLoad {
    [super viewDidLoad];
    NSURL *url = [NSURL URLWithString:@"http://www.greyhoundtv.org"];
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    [webView loadRequest:request];
    // Do any additional setup after loading the view.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

- (IBAction)reload:(id)sender {
    NSURL *url = [NSURL URLWithString:@"http://www.gilmannewsapp.squarespace.com/gtv"];
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    [webView loadRequest:request];
}
@end
