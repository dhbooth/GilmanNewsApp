//
//  ontwo.m
//  The Gilman News 5.0
//
//  Created by Davis Booth on 9/11/16.
//  Copyright © 2016 Davis Booth. All rights reserved.
//

#import "ontwo.h"

@interface ontwo ()

@end

@implementation ontwo

- (void)viewDidLoad {
    [super viewDidLoad];
    NSURL *url = [NSURL URLWithString:@"http://www.gilmannews.com/2001-2002"];
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

- (IBAction)back:(id)sender {
    NSURL *url = [NSURL URLWithString:@"http://www.gilmannews.com/2001-2002"];
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    [webView loadRequest:request];
}
@end
